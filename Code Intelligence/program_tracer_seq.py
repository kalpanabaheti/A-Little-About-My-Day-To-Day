import io
import os
import ast
import bdb
import sys
import json
import numbers
import argparse

from collections import defaultdict
from user_names_collector import UserNamesCollector
from assignment_collector import AssignmentCollector


class Value:
    """
    Value taken on by a variable on a particular line
    """

    def __init__(self, variable, lineno, value):
        self.variable = variable
        self.lineno = lineno
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Value):
            return False
        return self.value == other.value

    def __str__(self):
        return f"(line={self.lineno}, val={self.value})"

    def __repr__(self):
        return f"(line={self.lineno}, val={self.value})"


class ProgramTracer(bdb.Bdb):

    RETURN = "@return"

    def __init__(self, skip=None):
        super(ProgramTracer, self).__init__(skip)
        self._init()

    def _init(self):
        self.user_defined_names = {"<module>"}
        self.traces = {}
        self.prev_line = None
        # Line stack per context
        self.line_stack = defaultdict(list)
        self.line2vars = {}

    def trace(self, program, stdin=None):
        if stdin is not None:
            assert isinstance(stdin, list)
            sys.stdin = io.StringIO("\n".join(map(str, stdin)) + "\n")
        self._init()
        # Superfluous 'pass' so that trace for last statement is shown
        program += "\npass"
        tree = ast.parse(program)
        # Could we use 'frame.f_code.co_varnames' for variable names instead?
        unc = UserNamesCollector()
        unc.visit(tree)
        ac = AssignmentCollector()
        ac.visit(tree)
        self.line2vars = ac.line2vars
        self.user_defined_names.update(unc.user_names)
        self.run(program, globals=None, locals=None)

    def dispatch_call(self, frame, arg):
        func_name = frame.f_code.co_name
        if func_name in self.user_defined_names:
            return self.trace_dispatch

    def user_return(self, frame, return_value):
        if not return_value:
            return
        ctx = frame.f_code.co_name
        value = Value(self.RETURN, frame.f_lineno, return_value)
        self._add_value(value, ctx, self.RETURN)
        self._update_traces(ctx, frame)

    def user_line(self, frame):
        ctx = frame.f_code.co_name
        self._update_traces(ctx, frame)
        self.line_stack[ctx].append(frame.f_lineno)

    def _get_line(self, ctx, frame):
        try:
            return self.line_stack[ctx][-1]
        except:
            prev_ctx = frame.f_back.f_code.co_name
            return self.line_stack[prev_ctx][-1]

    def _update_traces(self, ctx, frame):
        for name, val in frame.f_locals.items():
            if not (name in self.user_defined_names and self._is_supported_type(val)):
                continue
            value = Value(name, self._get_line(ctx, frame), val)
            self._add_value(value, ctx, name)

    def _get_trace(self, ctx):
        ctx_traces = self.traces.get(ctx, [])
        if len(ctx_traces) == 0:
            self.traces[ctx] = ctx_traces
        return ctx_traces

    def _add_value(self, val: Value, ctx, name):
        trace = self._get_trace(ctx)
        # Check that name is a variable being assigned
        if name in self.line2vars[val.lineno].union({self.RETURN}):
            trace.append(val)

    @staticmethod
    def _is_supported_type(val):
        supported = (numbers.Number, str, bool)
        return isinstance(val, supported)

    @staticmethod
    def _equal(val1, val2):
        try:
            return val1.equals(val2)
        except:
            return val1 == val2


from multiprocessing import Process, Queue


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def trace_program(queue, program, user_input):
    try:
        sys.stdout = None
        tracer = ProgramTracer()
        tracer.trace(program, stdin=user_input)
        queue.put(tracer.traces)
    except:
        queue.put({})


def generate_program_traces(input_path, output_path, user_input=None):
    def get_files_in_path(path):
        for f in os.listdir(path):
            if f.endswith(".py"):
                yield f

    files_and_programs = []
    for file in get_files_in_path(input_path):
        try:
            program = read_file(f"{input_path}/{file}")
            files_and_programs.append((file, program))
        except:
            continue

    results = []
    for filename, program in files_and_programs:
        try:
            print(f"Processing file {filename}...")
            queue = Queue()
            p = Process(target=trace_program, args=(queue, program, user_input))
            p.start()
            p.join(timeout=2)
            result = queue.get()
            traces = []
            for k, v in result.items():
                traces.append(
                    {
                        "context": k,
                        "seq": [
                            {
                                "variable": val.variable,
                                "lineno": val.lineno,
                                "value": val.value,
                            }
                            for val in v
                        ],
                    }
                )
            if traces:
                results.append({"filename": filename, "trace": traces})
        except:
            print(f"[ERROR] Could not process {filename}")

    for res in results:
        filename = res["filename"]
        try:
            file_wo_ext = filename[: filename.index(".")]
            with open(f"{output_path}/{file_wo_ext}.json", "w") as jf:
                json.dump(res, jf, indent=2)
        except:
            print(f"[ERROR] Could not save {filename}")


if __name__ == "__main__":
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--assignment", help="Folder where submissions are located", type=str
    )
    parser.add_argument(
        "-o", "--out", help="Folder where output should be produced", type=str
    )
    parser.add_argument(
        "-i", "--input", nargs="+", help="List to be used as stdin", type=str
    )
    args = parser.parse_args()
    '''
    ip = input("\nEnter input path: ")
    op = input("\nEnter output path: ")
    argument = input("\nEnter argument: ")
    generate_program_traces(ip,op,list(argument))

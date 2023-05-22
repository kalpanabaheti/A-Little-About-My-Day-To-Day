$(document).ready(function() {

    $.getJSON('static/diseases.json').then(function (response) {
        console.log(response)
      $('.js-disease').select2({
        placeholder: 'Search for a disease',
        data: response.results
      });
    });


    $.getJSON("static/drugs.json").then(function (response) {
        console.log(response)
      $('.js-drugs').select2({
        placeholder: 'Search for a drug',
        data: response.results
      });
    });

    $('#calculate').click(function(){
        function getNames(item) {
            return item.text
        }
        $('#table').hide()
        $('#results').hide()
        var disease_selection = $('.js-disease').select2('data').map(getNames);
        var drug_selection = $('.js-drugs').select2('data').map(getNames);
       // posting the selections, awaiting a result
        $.ajax({
            type: 'POST',
            url: "/process",
            data: JSON.stringify([disease_selection, drug_selection]),
            contentType: "application/json",
            dataType: 'json',
            success: function(result) {
                $('#table').show();
                console.log(result)
            }
        })
    });


    $('#table').click(function(){
        $.getJSON("static/output_file.json", function(json) {
            $('#results').show()
            var jsonData = json;
            let container = $("#container");
             document.getElementById('container').innerHTML = "";
             // Create the table element
             let table = $("<table>");
             // Get the keys (column names) of the first object in the JSON data
             let cols = Object.keys(jsonData[0]);
             // Create the header element
             let thead = $("<thead>");
             let tr = $("<tr>");
             // Loop through the column names and create header cells
             $.each(cols, function(i, item){
                let th = $("<th>");
                th.text(item); // Set the column name as the text of the header cell
                tr.append(th); // Append the header cell to the header row
             });
             thead.append(tr); // Append the header row to the header
             table.append(tr) // Append the header to the table
             // Loop through the JSON data and create table rows
             $.each(jsonData, function(i, item){
             let tr = $("<tr>");
                // Get the values of the current object in the JSON data
                let vals = Object.values(item);
                // Loop through the values and create table cells
                $.each(vals, (i, elem) => {
                   let td = $("<td>");
                   td.text(elem); // Set the value as the text of the table cell
                   tr.append(td); // Append the table cell to the table row
                });
                table.append(tr); // Append the table row to the table
             });
             container.append(table)});

        $.getJSON("static/vis_file.json", function(json) {
            const data = json;
            console.log(data);
            new Chart(
                document.getElementById('graphs'),
                {
                  type: 'bar',
                  data: {
                    labels: data.map(row => row.effect),
                    datasets: [
                      {
                        label: 'Aggregate Side Effects',
                        data: data.map(row => row.count),
                        backgroundColor: 'rgba(255, 99, 132, 0.2)'
                      }
                    ]
                  },
                  options: {
                    responsive:true,
                    scales: {
                      y: {suggestedMin: 0}
                    }
                  }
                }
              );

            });
      });
});

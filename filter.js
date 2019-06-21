$(document).ready(function(){
	$("#city").change(function(){
		let city = $("#city").val();
		$("table tr").remove();
		$("#bankTable").prepend(`
			<tr>
				<th>CITY</th>
				<th>District</th>
				<th>Branch</th>
				<th>Bank Name</th>
        <th>IFSC</th>
        <th>BANK ID</th>
        <th>STATE</th>
        <th>ADDRESS</th>
			</tr>`);
		$.getJSON(`https://vast-shore-74260.herokuapp.com/banks?city=${city}`, function(result){
                $.each(result, function(i, data){
                  //console.log(result)
                  //$("#content").append(`<option value="${data.programName}"> ${data.programName} </option>`);
                  $("#bankTable:last").append(`<tr>
                  		<td>${data.city}</td>
                  		<td>${data.district}</td>
                  		<td>${data.branch}</td>
                  		<td>${data.bank_name}</td>
                      <td>${data.ifsc}</td>
                      <td>${data.bank_id}</td>
                      <td>${data.state}</td>
                      <td>${data.address}</td>
                  		</tr>`);
                  //program = $("#PopulateProgram").val();                          
                });
              });
	});
});

// Search data in table 
function searchBranch() {
  // Declare variables 
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.getElementById("bankTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    } 
  }
}

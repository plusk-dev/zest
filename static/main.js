let form = document.getElementById("estimate_form");

const getTable = (data) => {
  let final = `
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.6.0/mdb.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="/static/dashboard.css">
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400&display=swap');
  .data-table {
    font-family: "Exo 2" !important;
  }
  </style>

  <div class="table-responsive" id="data-table">
  <h3 style="font-weight: lighter; text-align: center">Material Audit</h3>
   <span> Window Dimensions:</span><br>

  <b>Height</b>: ${data["Track - Vertical"]["total"] / 2} mm
  <br>
  <b>Width</b>: ${data["Track - Top/Bottom"]["total"] / 2} mm
  <table class="table table-bordered table-hover data-table" >
    <thead>
      <tr>
      
        <th scope="col"><b>Sr No.</b></th>
        <th scope="col"><b>Item Name</b></th>
        <th scope="col"><b>Per Piece Dimension</b></th>
        <th scope="col"><b>No. of Pieces</b></th>
        <th scope="col"><b>Material Dimensions</b></th>
        </tr>
    </thead>
    <tbody>
`;
  let names = Object.keys(data);
  for (const name of names) {
    let index = names.indexOf(name);
    let element = names[index];
    final += `
    <tr>
    <th scope="row"><b>${index + 1}<b></th>
    <td>${element}</td>
    <td>${data[name]["per_piece"]} ${data[name]["Unit"]}</td>
    <td>${data[name]["Pieces"]}</td>
    <td>${data[name]["total"]} ${data[name]["Unit"]}</td>
    </tr>
  
`;
  }
  return final;
};

form.addEventListener("submit", (e) => {
  e.preventDefault();
  let data_table = document.getElementById("data-table");
  data_table.innerHTML = "Loading....";
  let form_data = new FormData(form);
  let height = form_data.get("height");
  let width = form_data.get("width");
  let api_call_url = `/estimate?width=${width}&height=${height}`;
  fetch(api_call_url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      data_table.innerHTML = getTable(data);
      let orderForm = document.getElementById("order-form");
      orderForm.style.display = "";
      orderForm.addEventListener("submit", (e) => {
        e.preventDefault();
        let orderFormData = new FormData(orderForm);
        let orderName = orderFormData.get("name");
        fetch(`/estimate/create_order`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            "username": orderFormData.get("username"),
            "password": orderFormData.get("password"),
            "name": orderFormData.get("name"),
            "order_data": data
          })
        }).then(response => response.json()).then(resdata => {
          if (resdata.message != "error") {
            window.location = `/dashboard/order?id=${resdata.order_data.id}`
          } else {
            document.getElementById("confirm-order-btn").classList.toggle("btn-danger")
          }
        })
      });
      document.getElementById("print-btn").style.display = "";
      document.getElementById("print-btn").addEventListener("click", (e) => {
        let divContents = document.getElementById("data-table").innerHTML;
        let printWindow = window.open();
        printWindow.document.write(divContents);
        printWindow.document.close();
        printWindow.print();
      });
    });
});

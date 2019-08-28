$("#trackerForm").submit(function (event) {
    var formData = {
        'orderId': $('input[name=idTrack]').val(),
        'email': $('input[name=emailTrack]').val(),
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    };
    $.ajax({
        type: 'POST',
        url: '/market/tracker/',
        data: formData,
        encode: true
    })
        .done(function (data) {
            data = JSON.parse(data);
            if (Object.keys(data).length > 0) {
                let itemsObject = JSON.parse(data.itemsJson)
                let items = `<ul class="list-group">`;
                for (i in itemsObject) {
                    items += `<li class="list-group-item d-flex justify-content-between align-items-center">`+ itemsObject[i][1] +`<span class="badge badge-primary badge-pill">`+ itemsObject[i][0] + `</span>
              </li>`
                }
                items += `</ul>`;
                var trackContent = `<p class='lead'>Your Order Status: ` + data['order_status'] + `</p><p class="lead">Date of order: ` + data['timestamp'] + `</p>`
                $('#items').html(trackContent + items);
            }
            else {
                $('#items').html("data Not Found");
            }
        });
    event.preventDefault();
}
)
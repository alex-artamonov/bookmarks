const url = '{% url "images:like" %}'
var options = {
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
    mode: 'same-origin'
}
document.querySelector('a.like')
        .addEventListener('click', function(e){
    e.preventDefault();
    var likeButton = this;
// request body
var formData = new FormData();
formData.append('id', likeButton.dataset.id);
formData.append('action', likeButton.dataset.action)
options['body'] = formData;
// send HTTP request
fetch(url, options)
 .then(response => response.json())
 .then(data => {
    if (data['status'] === 'ok')
    {
      var previousAction = likeButton.dataset.action;
      var action = previousAction === 'like' ? 'unlike' : 'like';
      likeButton.dataset.action = action;
      likeButton.innerHTML = action;
      var likeCount = document.querySelector('span.count .total')
      var totalLikes = parseInt(likeCount.innerHTML);
      likeCount.innerHTML = previousAction === 'like' ? totalLikes + 1 : totalLikes - 1;
    }
 })
});
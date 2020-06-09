$(document).ready(()=>{
    if($("#posts").children().length == 0){
        $("#posts").append("<p class='alert alert-warning'>Sorry, no posts for now!!</p>")
    }
})
function comment(btn){
        var form = $( btn ).parentsUntil('div[class=card]').children('#commentForm') 
        form.find('textarea').focus()
        //form.find('textarea').focus()
        form.toggle()
        form.submit(function(e){
            e.preventDefault()
            form.find("#subcommentbtn").html(`<button class='btn btn-primary' disabled>Posting 
            <img src = "/static/spinners/posting.gif" id="loading" style="display: none;"
            width="30px" height="30px"></button>`) 
            form.find("#loading").css('display','inline')
            var dat = new FormData(e.target)
            var post = dat.get('post')
            comment = dat.get('comment')
            console.log(post)
            $.ajax({
                url : 'post/comment/',
                method : 'POST',
                data : {
                    comment : comment,
                    post : post,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                }
            }).done(data=>{
                location.href = data
            })
        })
}

function like(btn){
    parents = $(btn).closest('div[class=card]')
    id = parents.children('input[name=postid]').val()
    $.ajax({
        method : "POST",
        url : "post/like/",
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
            id : id
        }
    }).done(data=>{
        parents.find('p[id=showLikes]').text(`Likes : ${data}`)
    })
}
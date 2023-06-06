from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product, Comment, Clothes,ClotheCategory
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'pages/product_detail.html', {'product': product})


def clothe_detail(request, product_id):
    clothe = get_object_or_404(Clothes, id=product_id)
    return render(request, 'pages/clothes_detail.html', {'clothe': clothe})


@login_required(login_url='login')
def new_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        Comment.objects.create(
            author = request.user,
            product = product,
            body = request.POST['body'],
        )
        messages.info(request, 'Successfully Sended')
        return redirect ('product:product_detail', product_id)
    return HttpResponse('add comment')

@login_required(login_url='login')
def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.info(request, 'Successfully Deleted')
        return redirect ('product:product_detail', product_id)
    return redirect ('product:product_detail', product_id)
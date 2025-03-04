from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    # Obtem a postagem com base no ID
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Formulario foi submetido
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Campos do formulario passaram pela validacao
            cd = form.cleaned_data
            # ... envia o email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recomenda a leitura de {post.title}"
            message = f"Leia {post.title} em {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'emanuel.angelo16@gmail.com', [cd['to']]) # Aqui deve ser colocado o email do remetente
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 postagens em cada pagina
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Se a pagina nao for um inteiro, retorne a primeira pagina
        posts = paginator.page(1)
    except EmptyPage:
        # Se a pagina esta fora do intervalo, retorne a ultima pagina de resultados
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})
    


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,FormView,CreateView
from .forms import InventoryUpdateForm,ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import InventoryPost
from .forms import InventoryPostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(ListView):
    template_name='index.html'
    context_object_name = 'orderby_records'

    queryset=InventoryPost.objects.order_by('-posted_at')
    paginate_by=10

class InventoryDetail(DetailView):
    template_name='post.html'
    model=InventoryPost
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InventoryUpdateForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = InventoryUpdateForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory_detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))
class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = InventoryPost
    form_class = InventoryPostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('inventory:index')
    login_url = '/login/'   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class InventoryDeleteView(LoginRequiredMixin,DeleteView):
    model=InventoryPost
    template_name='inventory_delete.html'
    success_url= reverse_lazy('inventory:index')
    login_url ='/login/'
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
class Daily_necessitiesView(ListView):
    template_name ='daily_necessities_list.html'
    model = InventoryPost
    context_object_name = 'daily_necessities_records'    
    queryset = InventoryPost.objects.filter(
        category='日用品').order_by('-posted_at')
    paginate_by = 10

class Daily_goodsView(ListView):
    template_name ='daily_goods_list.html'
    model = InventoryPost
    context_object_name = 'daily_goods_records'
    queryset = InventoryPost.objects.filter(
        category='生活用品').order_by('-posted_at')
    paginate_by = 10

class GroceriesView(ListView):
    template_name ='groceries_list.html'
    model = InventoryPost
    context_object_name = 'groceries_records'
    queryset = InventoryPost.objects.filter(
        category='食料品').order_by('-posted_at')
    paginate_by = 10


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('inventory:contact')

    def form_valid(self,form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\nタイトル:{2}\n メッセージ:\n{3}'\
                .format(name,email,title,message)
        from_email = 'te2195094@gmail.com'
        to_list= ['te2195094@gmail.com']
        message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(
            self.request,'お問い合わせは正常に送信されました。')
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
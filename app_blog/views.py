from _csv import reader
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from app_blog.forms import UploadRecordForm, BlogRecordForm
from app_blog.models import BlogRecordModel, BlogImgModel


class CreateRecordView(View):
    def get(self, request):
        if request.user.is_authenticated:
            create_form = BlogRecordForm()
        else:
            raise PermissionDenied
        return render(request=request, template_name='create.html', context={'create_form': create_form})

    def post(self, request):
        create_form = BlogRecordForm(request.POST, request.FILES)
        if create_form.is_valid():
            images = request.FILES.getlist('images')
            description = create_form.cleaned_data['description']
            blog = BlogRecordModel.objects.create(user=request.user, description=description)
            for img in images:
                instance = BlogImgModel(images=img, blog_record_id=blog.id)
                instance.save()
            blog.save()
            return redirect('/')
        return render(request=request, template_name='create.html', context={'create_form': create_form})

class ListRecordView(ListView):
    def get_queryset(self):
        record_qs = BlogRecordModel.objects.all().order_by('-date_creation')
        return record_qs

    model = BlogRecordModel
    template_name = 'record_list.html'
    context_object_name = 'record_list'

class RecordDetailView(View):
    def get(self, request, pk):
        record_info = BlogRecordModel.objects.get(id=pk)
        img_record = BlogImgModel.objects.filter(blog_record_id=pk)
        return render(request=request, template_name='record_detail.html', context={'record':record_info, 'imgs':img_record})

    def post(self, request, pk):
        BlogRecordModel.objects.filter(id=pk).delete()
        return redirect('/blog/records/')

class UploadRecordView(View):
    def get(self, request):
        if request.user.is_authenticated:
            upload_rec = UploadRecordForm()
        else:
            raise PermissionDenied
        return render(request=request, template_name='upload.html', context={'upload':upload_rec})

    def post(self, request):
        upload_rec = UploadRecordForm(request.POST, request.FILES)

        if upload_rec.is_valid():
            file_rec = upload_rec.cleaned_data['file'].read()
            rec_str = file_rec.decode('utf-8').split('\r\n')
            csv_reader = reader(rec_str, delimiter=":", quotechar='"')
            for row in csv_reader:
                if row == []:
                    continue
                else:
                    row = row[0].split(';')
                    BlogRecordModel.objects.create(description=row[0], date_creation=row[1], user=request.user)
            upload_rec.save()
            return render(request=request, template_name='upload.html', context={'upload':upload_rec})

from django.shortcuts import redirect, render

from .forms import UploadFileForm

from .services import *


# Create your views here.


def show_uploads_page(request):
    # process POST request
    if request.method == 'POST':

        if handle_uploaded_file(request.FILES.get('file1', None), request.FILES.get('file1', None).name):
            if handle_uploaded_file(request.FILES.get('file2', None), request.FILES.get('file2', None).name):
                update_data_file_names(request)
                if check_data_files(request):
                    features_table = get_features_table_preview(request)
                    target_table = get_target_table_preview(request)
                    form = UploadFileForm()
                    return render(request, 'uploads/upload.html', {'form': form, 'features': features_table, 'target': target_table})


        # process GET request
    form = UploadFileForm()
        # initialize session variables
    initialize_data_file_names(request)
    return render(request, 'uploads/upload.html', {'form': form})




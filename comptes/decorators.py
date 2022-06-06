from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
import six

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('connexion')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group= None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Non autorisé")

            print('Working', allowed_roles)
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "client":
            return redirect("home")

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function



def group_required(group, login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        
        if user.groups.filter(name__in=groups).exists():
            return True
        if raise_exception:
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url=login_url)

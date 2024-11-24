def user_info(request):
    if request.user.is_authenticated:
        return {
            'user_name': request.user.first_name
        }
    return {}

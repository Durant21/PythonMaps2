from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.pt')
def my_view(request):
    return {'project': 'PythonMaps2'}

#
# @view_config(route_name='v2', renderer='../templates/template5.pt')
# def about_view(request):
#     return {'project': 'PythonMaps2'}
#

@view_config(route_name='testko', renderer='../templates/PythonMaps/template_DataLoader.pt')
def ko_view(request):
    return {'project': 'PythonMaps2'}
from common import response_helper


def find_project_page(request):
    """
    找项目页面
    :param request:
    :return:
    """
    data = {}
    data["classify"] = {}
    
    return response_helper.render_response_html(request, 'project/find_project.html', {})

from django.views.decorators.csrf import ensure_csrf_cookie

from common import response_helper
from . import logic


@ensure_csrf_cookie
def find_project_page(request):
    """
    找项目页面
    :param request:
    :return:
    """
    classify_second_guid = request.GET.get("classify_second_guid")
    data = dict()
    data['classify_first_list'] = logic.get_project_classify()
    data['project_list'] = logic.get_project_list(classify_second_guid)
    data['show_classify_first_guid'] = logic.get_classify_first_by_classify_second(classify_second_guid)

    return response_helper.render_response_html(request, 'project/find_project.html', data)


@ensure_csrf_cookie
def project_info(request):
    """
    项目详情页面
    :param request:
    :return:
    """
    project_guid = request.GET.get("project_guid")
    data = dict()
    data['project_info'] = logic.get_project_info(project_guid)

    return response_helper.render_response_html(request, 'project/project_info.html', data)

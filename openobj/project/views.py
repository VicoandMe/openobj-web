from common import response_helper
from . import logic


def find_project_page(request):
    """
    找项目页面
    :param request:
    :return:
    """
    classify_second_id = request.GET.get("classify_second_id")
    data = dict()
    data['classify_first_list'] = logic.get_project_classify()
    data['project_list'] = logic.get_project_list(classify_second_id)
    data['show_classify_first_id'] = logic.get_classify_first_by_classify_second(classify_second_id)

    return response_helper.render_response_html(request, 'project/find_project.html', data)


def project_info(request):
    """
    项目详情页面
    :param request:
    :return:
    """
    project_id = request.GET.get("project_id")
    data = dict()
    data['project_info'] = logic.get_project_info(project_id)

    return response_helper.render_response_html(request, 'project/project_info.html', data)

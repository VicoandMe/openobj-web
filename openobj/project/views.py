from common import response_helper
from . import logic


def find_project_page(request):
    """
    找项目页面
    :param request:
    :return:
    """
    classify_second_id = request.GET.get("classify_second_id")
    data = {}
    data['classify_first_list'] = logic.get_project_classify()
    data['project_list'] = logic.get_project_list(classify_second_id)

    return response_helper.render_response_html(request, 'project/find_project.html', data)


def project_list_classify(request):
    """
    根据分类获取项目列表
    :param request:
    :return:
    """
    classify_second_id = request.GET.get("classify_second_id")
    print(classify_second_id)
    return

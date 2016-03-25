from common import const
from project.models import ProjectClassifyFirst, ProjectClassifySecond, Project


def get_project_classify_first():
    data = ProjectClassifyFirst.objects.all().values('guid', 'name')
    return list(data)


def get_project_classify_second(classify_first_guid):
    data = ProjectClassifySecond.objects.filter(classify_first__guid=classify_first_guid).values('guid', 'name')
    return list(data)


def get_project_classify():
    """
    获取所有分类信息
    :rtype: object
    """
    data = get_project_classify_first()
    for classify_first in data:
        classify_second = get_project_classify_second(classify_first['guid'])
        classify_first['classify_second'] = classify_second
    return data


def get_project_list(classify_second_guid=None):
    """
    获取项目列表
    :param classify_second_guid: 二级分类id
    :return:
    """
    if classify_second_guid:
        try:
            classify_second = ProjectClassifySecond.objects.get(guid=classify_second_guid)
            project_list = classify_second.project_set.all()
            data = project_list.all()
            return list(data)
        except:
            return list()
    else:
        data = Project.objects.all()
        return list(data)


def get_classify_first_by_classify_second(classify_second_guid):
    """
    由二级分类id获取一级分类的id
    :param classify_second_guid:
    :return:
    """
    if classify_second_guid:
        classify_second = ProjectClassifySecond.objects.get(guid=classify_second_guid)
        return classify_second.classify_first.guid


def get_project_info(project_guid):
    """
    获取项目信息
    :param project_guid:
    :return:
    """
    if project_guid:
        data = Project.objects.get(guid=project_guid)
        return data

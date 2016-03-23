from common import const
from project.models import ProjectClassifyFirst, ProjectClassifySecond


def get_project_classify_first():
    data = ProjectClassifyFirst.objects.all().values('guid', 'name')
    return const.SUCCESS_STATUS, 'OK', list(data)

def get_project_classify():
    project_classify_list = ProjectClassifySecond.objects.all()
    data = dict()
    for classify in project_classify_list:
        data['first_classify_id'] = classify.classify_first.guid
        data['first_classify_name'] = classify.classify_first.name
        tmp_dict = dict()
        tmp_dict[]

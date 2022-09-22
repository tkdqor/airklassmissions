from rest_framework.serializers import ModelSerializer

from .models import Klass


class KlassModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    create 메소드를 통해 로그인된 강사로 1:N 관계에 있는 Klass 모델 객체를 생성합니다.
    """

    def create(self, validated_data):
        master = self.context["master"]
        klass = Klass(master=master, **validated_data)
        klass.save()
        return klass

    class Meta:
        model = Klass
        fields = ("master", "title", "summary", "created_at")
        read_only_fields = ["master", "created_at"]

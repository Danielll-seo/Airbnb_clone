from django.db import models

# 다른 앱들을 위한 공통 모델을 정의하는 파일입니다.
class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True 
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # .ImageField - need Pillow(pip3 install Pillow)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        # 상위클래스의 save방식을 바꾼다?
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''
    Pillow를 사용하여 django로 들어오는 이미지를 모두 재조정하여 저장해놓기
    - 고해상도의 이미지는 브라우저에서 불러올 때 오래걸리기 때문
'''
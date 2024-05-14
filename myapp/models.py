from django.db import models
from django.utils.safestring import mark_safe


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)
    dp = models.ImageField(upload_to="profile")


    def profile(self):
        return mark_safe('<img src="{}" width="100">'.format(self.dp.url))

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class serviceCategories(models.Model):
    image = models.ImageField(upload_to="ServiceCategories")
    catename = models.CharField(max_length=100)

    def __str__(self):
        return self.catename

    def category(self):
        return mark_safe('<img src="{}" width="100">'.format(self.image.url))


class Services(models.Model):
    cate = models.ForeignKey(serviceCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    desc = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Services", null=True, blank=True)
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def ServicePhoto(self):
        return mark_safe('<img src="{}" width="100">'.format(self.image.url))


    def __str__(self):
        return self.name


class serviceInquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serviceId = models.ForeignKey(Services, on_delete=models.CASCADE)
    subject = models.CharField(max_length=60)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


class courcesCategories(models.Model):
    image = models.ImageField(upload_to="ServiceCategories")
    catename = models.CharField(max_length=100)

    def __str__(self):
        return self.catename

    def category(self):
        return mark_safe('<img src="{}" width="100">'.format(self.image.url))


class Cource(models.Model):
    cate = models.ForeignKey(courcesCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    desc = models.TextField()
    duration = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    totalStudents = models.IntegerField()
    image = models.ImageField(upload_to="Cources", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    timings = models.CharField(max_length=200)

    def CourcePhoto(self):
        return mark_safe('<img src="{}" width="100">'.format(self.image.url))


class courceInquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courceId = models.ForeignKey(Cource, on_delete=models.CASCADE)
    subject = models.CharField(max_length=60)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user}"


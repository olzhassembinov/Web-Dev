from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

    @classmethod
    def create_test_data(cls):
        if not cls.objects.exists():
            company1 = cls.objects.create(
                name="StartHub.kz",
                description="A crowdfunding platform in Kazakhstan that supports socially important projects and innovations in all the spheres.",
                city="Almaty",
                address="Tole bi st. 59"
            )
            company2 = cls.objects.create(
                name="Zyan GAMES",
                description="We are indie game developer studio who makes open source games",
                city="Astana",
                address="Mangilik-el av. 1"
            )
            
            # Создаем тестовые вакансии
            Vacancy.create_test_data(company1, company2)

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return f"{self.name} ({self.salary})"

    @classmethod
    def create_test_data(cls, company1, company2):
        if not cls.objects.exists():
            cls.objects.create(
                name="Frontend Developer",
                description="Looking for an experienced frontend developer",
                salary=150000,
                company=company1
            )
            cls.objects.create(
                name="Backend Developer",
                description="Looking for an experienced backend developer",
                salary=180000,
                company=company1
            )
            cls.objects.create(
                name="Game Designer",
                description="Looking for a creative game designer",
                salary=120000,
                company=company2
            )

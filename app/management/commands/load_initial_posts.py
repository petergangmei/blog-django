from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Post
from django.utils.timezone import make_aware
from datetime import datetime

class Command(BaseCommand):
    help = 'Load initial posts data'

    def handle(self, *args, **kwargs):
        # Get or create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            email='admin@example.com',
            is_staff=True,
            is_superuser=True
        )
        if created:
            admin_user.set_password('admin')
            admin_user.save()

        # Initial posts data
        posts_data = [
            {
                "title": "Test Post",
                "content": "This is a test post content.",
                "created_at": "2025-04-07T11:35:32.000Z",
                "updated_at": "2025-04-07T11:35:32.000Z"
            },
            {
                "title": "hey jianlu",
                "content": "i love you",
                "created_at": "2025-04-07T11:38:08.000Z",
                "updated_at": "2025-04-07T11:38:08.000Z"
            },
            {
                "title": "hey jianlu",
                "content": "i love you",
                "created_at": "2025-04-07T11:38:14.000Z",
                "updated_at": "2025-04-07T11:38:14.000Z"
            },
            {
                "title": "hey jianlu",
                "content": "i love you",
                "created_at": "2025-04-07T11:38:16.000Z",
                "updated_at": "2025-04-07T11:38:16.000Z"
            }
        ]

        # Create posts
        for post_data in posts_data:
            Post.objects.create(
                title=post_data['title'],
                content=post_data['content'],
                created_at=make_aware(datetime.strptime(post_data['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')),
                updated_at=make_aware(datetime.strptime(post_data['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ')),
                user=admin_user
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial posts data')) 
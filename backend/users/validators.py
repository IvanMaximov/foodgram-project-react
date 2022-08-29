from rest_framework import serializers


def self_subscription_validator(self, request, *args, **kwargs):
    if self.kwargs.get('user_id') == request.user.id:
        raise serializers.ValidationError('Нельзя подписываться на себя')

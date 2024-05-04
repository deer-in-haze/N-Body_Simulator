import pytest
from animation_settings import AnimationSettings


@pytest.fixture
def default_animation_settings():
    return AnimationSettings.Builder().build()


@pytest.fixture
def custom_animation_settings():
    builder = AnimationSettings.Builder()
    builder.set_lines(False)
    builder.set_frames(100)
    builder.set_interval(10)
    builder.set_blit(True)
    return builder.build()


def test_default_settings(default_animation_settings):
    assert default_animation_settings.get_lines() == True
    assert default_animation_settings.get_frames() == 200
    assert default_animation_settings.get_interval() == 20
    assert default_animation_settings.get_blit() == False


def test_custom_settings(custom_animation_settings):
    assert custom_animation_settings.get_lines() == False
    assert custom_animation_settings.get_frames() == 100
    assert custom_animation_settings.get_interval() == 10
    assert custom_animation_settings.get_blit() == True


def test_setting_modifications():
    settings = AnimationSettings.Builder()
    settings.set_lines(False).set_frames(300).set_interval(30).set_blit(True)
    animation_settings = settings.build()

    assert animation_settings.get_lines() == False
    assert animation_settings.get_frames() == 300
    assert animation_settings.get_interval() == 30
    assert animation_settings.get_blit() == True

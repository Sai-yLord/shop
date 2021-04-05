from django import template
from django.utils.safestring import mark_safe
# from mainapp.models import *


register = template.Library()

TABLE_HEAD = """
            <table class="table">
                <tbody>
            """

TABLE_TAIL = """
                </tbody>
            </table>  
            """

TABLE_CONTENT = """
                <tr>
                    <td>{name}</td>
                    <td>{value}</td>
                  </tr>
                """

PRODUCT_SPECTOR = {
    "notebook": { 
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота Процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video_card',
        'Время работы аккумулятора': 'time_without_charge'
    },
    "smartphone": { 
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение Экрана': 'resolution',
        'Объем Батаерии': 'accum_volume',
        'Оперативная память': 'ram',
        'SD': 'sd',
        'Максимальный Объем Sd': 'sd_volume_max',
        'Главная Камера': 'main_cam_mp',
        'Фронтальная Камера': 'frontal_cam_mp'
    }
}

def get_product_spector(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPECTOR[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content

@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    # if model_name == 'smartphone':
    #     if not product.sd:
    #         PRODUCT_SPECTOR["smartphone"].pop('Максимальный Объем Sd')
    # if isinstance(product, Smartphone):
    #     if not sd:
    #         PRODUCT_SPECTOR["smartphone"].pop("Максимальный Объем Sd")
    #     else:
    #         PRODUCT_SPECTOR["smartphone"]['Максимальный Объем Sd'] = "sd_volume_max"
    return mark_safe(TABLE_HEAD + get_product_spector(product, model_name) + TABLE_TAIL)


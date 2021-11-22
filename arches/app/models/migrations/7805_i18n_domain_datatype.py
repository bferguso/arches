# Generated by Django 2.2.13 on 2021-03-19 20:17
from arches.app.models.fields.i18n import I18n_JSONField
from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ("models", "7794_i18n_string_datatype"),
    ]

    sql = """
        UPDATE public.cards_x_nodes_x_widgets
        SET config =
        jsonb_set(config, '{{placeholder}}', json_build_object('{0}', config->>'placeholder')::jsonb, true)||
        '{{"i18n_properties": ["placeholder"]}}'
        WHERE nodeid in (SELECT nodeid FROM nodes WHERE datatype = 'domain-value' OR datatype = 'domain-value-list');

        UPDATE public.widgets
        SET defaultconfig = defaultconfig ||
            jsonb_set(defaultconfig, '{{placeholder}}', json_build_object('{0}', defaultconfig->>'placeholder')::jsonb, true) ||
        '{{"i18n_properties": ["placeholder"]}}'
        WHERE datatype = 'domain-value' OR datatype = 'domain-value-list';

    """.format(
        settings.LANGUAGE_CODE
    )

    reverse_sql = """
        UPDATE public.cards_x_nodes_x_widgets
        set config = config - 'i18n_properties' ||
        json_build_object('placeholder', jsonb_extract_path(config, 'placeholder', '{0}'))::jsonb
        WHERE nodeid in (SELECT nodeid FROM nodes WHERE datatype = 'domain-value' OR datatype = 'domain-value-list');

        UPDATE public.widgets
        SET defaultconfig = defaultconfig - 'i18n_properties' ||
        json_build_object('placeholder', jsonb_extract_path(defaultconfig, 'placeholder', '{0}'))::jsonb ||
        WHERE datatype = 'domain-value' OR datatype = 'domain-value-list';


    """.format(
        settings.LANGUAGE_CODE
    )

    operations = [
        migrations.RunSQL(sql, reverse_sql),
        migrations.AlterField(
            model_name="cardxnodexwidget",
            name="config",
            field=I18n_JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="widget",
            name="defaultconfig",
            field=I18n_JSONField(blank=True, null=True),
        ),
    ]

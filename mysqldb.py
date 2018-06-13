# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Geraet(models.Model):
    geraet_id = models.AutoField(primary_key=True)
    geraet = models.CharField(max_length=250)
    beschreibung = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geraet'


class Kunde(models.Model):
    kunde_id = models.AutoField(primary_key=True)
    nickname = models.CharField(unique=True, max_length=250)
    vorname = models.CharField(max_length=250)
    nachname = models.CharField(max_length=250)
    geschlecht = models.CharField(max_length=250)
    groesse_in_cm = models.FloatField()
    gewicht_in_g = models.FloatField()
    bmi = models.FloatField()

    class Meta:
        managed = False
        db_table = 'kunde'


class Muskelgruppe(models.Model):
    muskelgruppe_id = models.IntegerField(primary_key=True)
    bezeichnung = models.CharField(max_length=250)
    beschreibung = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'muskelgruppe'


class Sets(models.Model):
    set_id = models.AutoField(primary_key=True)
    uebung_uebung = models.ForeignKey('Uebung', models.DO_NOTHING, db_column='uebung_uebung_ID')  # Field name made lowercase.
    geraet_geraet = models.ForeignKey(Geraet, models.DO_NOTHING)
    wiederholung = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sets'
        unique_together = (('set_id', 'uebung_uebung', 'geraet_geraet'),)


class Texte(models.Model):
    text_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'texte'


class Trainingsplan(models.Model):
    trainingsplan_id = models.PositiveIntegerField(primary_key=True)
    erstelldatum = models.DateTimeField(blank=True, null=True)
    dauer_in_tagen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainingsplan'


class Uebung(models.Model):
    uebung_id = models.BigIntegerField(db_column='uebung_ID', primary_key=True)  # Field name made lowercase.
    uebung = models.CharField(max_length=250)
    beschreibung = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uebung'


class Wochentag(models.Model):
    wochentag_id = models.IntegerField(primary_key=True)
    wochentag = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wochentag'

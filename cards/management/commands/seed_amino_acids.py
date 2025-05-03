from django.core.management.base import BaseCommand
from cards.models import AminoAcidCard

class Command(BaseCommand):
    help = 'Добавляет 20 протеиногенных аминокислот в базу'

    def handle(self, *args, **kwargs):
        amino_acids_data = [
            {'name': 'Аланин', 'structure': 'CH3-CH(NH2)-COOH', 'code': 'Ala'},
            {'name': 'Аргинин', 'structure': 'H2N-C(NH)-NH-(CH2)3-CH(NH2)-COOH', 'code': 'Arg'},
            {'name': 'Аспарагин', 'structure': 'H2N-CO-CH2-CH(NH2)-COOH', 'code': 'Asn'},
            {'name': 'Аспарагиновая кислота', 'structure': 'HOOC-CH2-CH(NH2)-COOH', 'code': 'Asp'},
            {'name': 'Цистеин', 'structure': 'HS-CH2-CH(NH2)-COOH', 'code': 'Cys'},
            {'name': 'Глутамин', 'structure': 'H2N-CO-(CH2)2-CH(NH2)-COOH', 'code': 'Gln'},
            {'name': 'Глутаминовая кислота', 'structure': 'HOOC-(CH2)2-CH(NH2)-COOH', 'code': 'Glu'},
            {'name': 'Глицин', 'structure': 'H-CH(NH2)-COOH', 'code': 'Gly'},
            {'name': 'Гистидин', 'structure': 'C3H3N2-CH2-CH(NH2)-COOH', 'code': 'His'},
            {'name': 'Изолейцин', 'structure': '(CH3)2CH-CH2-CH(NH2)-COOH', 'code': 'Ile'},
            {'name': 'Лейцин', 'structure': '(CH3)2CH-CH2-CH(NH2)-COOH', 'code': 'Leu'},
            {'name': 'Лизин', 'structure': 'H2N-(CH2)4-CH(NH2)-COOH', 'code': 'Lys'},
            {'name': 'Метионин', 'structure': 'CH3-S-(CH2)2-CH(NH2)-COOH', 'code': 'Met'},
            {'name': 'Фенилаланин', 'structure': 'C6H5-CH2-CH(NH2)-COOH', 'code': 'Phe'},
            {'name': 'Пролин', 'structure': 'Пятичленный цикл с аминогруппой', 'code': 'Pro'},
            {'name': 'Серин', 'structure': 'HO-CH2-CH(NH2)-COOH', 'code': 'Ser'},
            {'name': 'Треонин', 'structure': 'CH3-CH(OH)-CH(NH2)-COOH', 'code': 'Thr'},
            {'name': 'Триптофан', 'structure': 'C8H6N-CH2-CH(NH2)-COOH', 'code': 'Trp'},
            {'name': 'Тирозин', 'structure': 'HO-C6H4-CH2-CH(NH2)-COOH', 'code': 'Tyr'},
            {'name': 'Валин', 'structure': '(CH3)2CH-CH(NH2)-COOH', 'code': 'Val'},
        ]

        for aa in amino_acids_data:
            obj, created = AminoAcidCard.objects.get_or_create(
                code=aa['code'],
                defaults={
                    'name': aa['name'],
                    'structure': aa['structure'],
                }
            )
            if created:
                self.stdout.write(f"Добавлена аминокислота: {aa['name']}")
            else:
                self.stdout.write(f"Амнокислота {aa['name']} уже есть в базе")
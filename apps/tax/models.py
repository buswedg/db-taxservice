from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.atoms import TimestampMixin


class TaxRate(TimestampMixin, models.Model):
    state = models.CharField(_('State'), max_length=2)
    zipcode = models.CharField(_('Zip Code'), max_length=5)
    tax_region_name = models.CharField(_('Tax Region Name'), max_length=100)
    estimated_combined_rate = models.DecimalField(_('Estimated Combined Rate'), max_digits=5, decimal_places=4)
    state_rate = models.DecimalField(_('State Rate'), max_digits=5, decimal_places=4)
    estimated_county_rate = models.DecimalField(_('Estimated County Rate'), max_digits=5, decimal_places=4)
    estimated_city_rate = models.DecimalField(_('Estimated City Rate'), max_digits=5, decimal_places=4)
    estimated_special_rate = models.DecimalField(_('Estimated Special Rate'), max_digits=5, decimal_places=4)
    risk_level = models.IntegerField(_('Risk Level'))

    class Meta:
        verbose_name = "Tax Rate"
        verbose_name_plural = "Tax Rate"
        ordering = ('state', 'tax_region_name', 'zipcode',)
        unique_together = ('state', 'zipcode', 'tax_region_name')

    def __str__(self):
        return self.tax_region_name

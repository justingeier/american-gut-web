#!/usr/bin/env python
from __future__ import division

# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The American Gut Project Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------


# Template specific dicts
_FAQ = {'FAQ_0_WHAT_IS_A_GUT': 'asdasdasd'}
_TAXA_SUMMARY = {'RESOLUTION_NOTE': "Note: Where there are blanks in the table below, the taxonomy could not be resolved in finer detail.",
                 'PERCENTAGES_NOTE': "Note: The percentages listed represent the relative abundance of each taxon. This summary is based off of normalized data. Because of limitations in the way the samples are processed, we cannot reliably obtain species level resolution. As such, the data shown are collapsed at the genus level.",
                 'DOWNLOAD_LINK': "Download the table"}
_HELP_REQUEST = {
    'CONTACT_HEADER': "Contact the American Gut",
    'RESPONSE_TIMING': "We will send a response to the email address you supply within 24 hours.",
    'FIRST_NAME': "First name",
    'LAST_NAME': "Last name",
    'EMAIL_ADDRESS': "Email address",
    'PROBLEM_PROMPT': "Enter information related to your problem"
}
_SAMPLE_OVERVIEW = {
    'BARCODE_RECEIVED': 'Sample %(barcode)s. This sample has been received by the sequencing center!',
    'DISPLAY_BARCODE': 'Sample %(barcode)s',
    'RESULTS_PDF_LINK': 'Click this link to visualize sample %(barcode)s in the context of other microbiomes!',
    'SAMPLE_NOT_PROCESSED': 'This sample has not yet been processed. Please check back later.',
    'DATA_VIS_TITLE': 'Data Visualization',
    'TAXA_SUM_TITLE': 'Taxa Summary',
    'VIEW_TAXA_SUMMARY': 'View Taxa Summary',
    'SAMPLE_STATUS': 'Sample Status',
    'SAMPLE_SITE': 'Sample Site',
    'SAMPLE_DATE': 'Sample Date',
    'SAMPLE_TIME': 'Sample Time',
    'SAMPLE_NOTES': 'Notes',
    'REMOVE_BARCODE': 'Remove barcode %(barcode)s'
}

# Actual text locale
text_locale = {
    'FAQ.html': _FAQ,
    'help_request.html': _HELP_REQUEST,
    'sample_overview.html': _SAMPLE_OVERVIEW,
    'taxa_summary.html': _TAXA_SUMMARY
    }

# Any media specific localizations
media_locale = {'LOGO': '/static/img/ag_logo.jpg',
                'PROJECT_TITLE': 'American Gut Project',
                'FAVICON': '/static/img/favicon.ico',
                'FUNDRAZR_URL': 'https://fundrazr.com/campaigns/4Tqx5',
                'NAV_PARTICIPANT_RESOURCES': 'Participant resources',
                'NAV_HOME': 'Home',
                'NAV_MICROBIOME_101': 'American Gut 101',
                'NAV_FAQ': 'FAQ',
                'NAV_MICROBIOME_FAQ': 'Human Microbiome FAQ',
                'NAV_ADDENDUM': 'How do I interpret my results?',
                'NAV_PRELIM_RESULTS': 'Preliminary results!',
                'NAV_CHANGE_PASSWORD': 'Change Password',
                'NAV_CONTACT_US': 'Contact Us',
                'NAV_LOGOUT': 'Log out',
                'NAV_HUMAN_SAMPLES': 'Human Samples',
                'NAV_RECEIVED': '(Received)',
                'NAV_ADD_HUMAN': 'Add Human Source',
                'NAV_ANIMAL_SAMPLES': 'Animal Samples',
                'NAV_ADD_ANIMAL': 'Add Animal Source',
                'NAV_ENV_SAMPLES': 'Environmental Samples',
                'NAV_LOG_SAMPLE': 'Log Sample',
                'NAV_JOIN_PROJECT': 'Join The Project',
                'NAV_KIT_INSTRUCTIONS': 'Kit Instructions',
                'NAV_PARTICIPANT_LOGIN': 'Participant Log In',
                'NAV_FORGOT_KITID': 'I forgot my kit ID',
                'NAV_FORGOT_PASSWORD': 'I forgot my password'
                }

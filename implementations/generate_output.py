# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CHAOSS
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Aniruddha Karajgi <akarajgi0@gmail.com>
#

import os
import shutil
import matplotlib.pyplot as plt
import json
import logging
from fpdf import FPDF


MD_FILE = 'report.markdown'
PDF_FILE = 'report.pdf'
JSON_FILE = 'report.json'
IMAGES_DIR = 'images'
MD_REPORT_TITLE = 'Metrics Report'
PDF_REPORT_TITLE = 'Metrics Report'

logger = logging.getLogger(__name__)


class GenerateOutput():
    """
    Class for generating output in different formats.

    :param results: A dictionary with the computed values of metrics,
        groups according to the category of metrics.

    :param output_formats: Possible formats for output. Currently, pdf,
        images, markdown and json are supported.

    :param write_to: The directory where the generated outputs are present.

    :param period: A string which can be any one of the pandas time
        series rules:
            'W': week
            'M': month
            'D': day

    """

    def __init__(self, results, output_formats=['json'], write_to='results_dir', period='M'):
        self.results = results
        self.output_formats = output_formats
        self.write_to = write_to
        self.period = period

        self.generate_options = {
            'markdown': self._generate_markdown,
            'json': self._generate_json,
            'pdf': self._generate_pdf,
            'images': self._generate_images
        }

    def generate(self):
        """
        Generates output in different formats.
        The generated outputs are stored in the write_to directory.

        write_to/
        ├── images
        │   └── metric1.png
        └── PDF_FILE
        └── JSON_FILE

        """

        logger.info("Generating results to %s" % self.write_to)
        if os.path.exists(self.write_to):
            shutil.rmtree(self.write_to)

        os.mkdir(self.write_to)
        for output_format in self.output_formats:
            self.generate_options[output_format]()

        logger.info("Finished generation")

    def _generate_pdf(self):
        """
        Generates a pdf report with results of the compute
        method as well as an image of the resultant plot.

        Creates PDF_FILE.
        """

        logger.info("Generating %s" % PDF_FILE)

        pdf = FPDF('P', 'mm', 'A4')
        pdf.set_font('Arial', 'B', 50)
        pdf.set_margins(left=20, top=20, right=-1)

        pdf.add_page()
        pdf.cell(w=100, h=100, txt=PDF_REPORT_TITLE, border=0, ln=2)

        pdf.set_font('Arial', 'B', 25)

        self._generate_images()

        for category, results_ in self.results.items():
            for result in results_:
                pdf.add_page()
                pdf.cell(w=100, h=10, txt=str(result['metric']), border=0, ln=1)
                pdf.ln()

                txt = \
                    """
                    The value of the metric is:\n
                    {}. \n
                    """.format(result['value'])
                pdf.set_font('Arial', style='', size=16)
                pdf.multi_cell(w=0, h=3, txt=txt)
                pdf.image(self.write_to + '/' + IMAGES_DIR + '/'
                          + "_".join(str(result['metric']).split()) + '.png', w=200)

        pdf.output(self.write_to + '/' + PDF_FILE, 'F')

    def _generate_markdown(self):
        """
        Generates a markdown report with results of the compute
        method as well as an image of the resultant plot.

        Creates MD_FILE.
        """

        logger.info("Generating %s" % MD_FILE)
        template = "# {}\n\n".format(MD_REPORT_TITLE)

        self._generate_images()

        for category, results_ in self.results.items():
            for result in results_:

                template += "## " + str(result['metric']) + '\n'

                txt = \
                    "The value of the metric is:\n" \
                    + "{}. \n".format(result['value'])

                template += txt

                embed_img = '![](../' + self.write_to + '/' + IMAGES_DIR + '/' \
                            + "_".join(str(result['metric']).split()) + '.png)'

                template += embed_img + "\n\n"

        with open(self.write_to + '/' + MD_FILE, 'w') as f:
            f.write(template)

    def _generate_json(self):
        """
        Generate a json file with results of metric computation,
        with each result on a new line.

        Creates JSON_FILE

        Format:
        {'category': 'commit', 'metric': <metric1>, 'value': <metric1_val>}
        {'category': 'commit', 'metric': <metric2>, 'value': <metric2_val>}
        {'category': 'issue', 'metric': <metric3>, 'value': <metric3_val>}
        ..
        .
        """

        logger.info("Generating %s" % JSON_FILE)

        with open(self.write_to + '/' + JSON_FILE, 'w') as json_file:
            for category, results_ in self.results.items():
                for result in results_:
                    json.dump({
                                'category': category,
                                'metric': str(result['metric']),
                                'value': str(result['value'])}, json_file)
                    json_file.write('\n')

    def _generate_images(self):
        """
        Generate charts as png images using pyplot.
        The generated images are stored in IMAGES_DIR.
        """

        logger.info("Generating charts to %s" % (IMAGES_DIR + '/'))

        if os.path.exists(self.write_to + '/' + IMAGES_DIR):
            shutil.rmtree(self.write_to + '/' + IMAGES_DIR)
        os.mkdir(self.write_to + '/' + IMAGES_DIR)
        for category, results_ in self.results.items():
            for result in results_:
                result['metric'].plot_time_series(self.period)
                plt.savefig(self.write_to + '/' + IMAGES_DIR + '/'
                            + "_".join(str(result['metric']).split()) + '.png')

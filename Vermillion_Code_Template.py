# DASC 511
# Project in Progress
# David M Vermillion
# 20 August 2022

# File initialization
pip install -r requirements.txt
import numpy as np
import pandas as pd
import math
import matplotlib as plt
import report_util
from astropy.io.votable import parse

# Import
votable = parse("PSCompPars_2022.08.14_13.46.20.votable")

# Data Transformations

## Unpack table columns desired for this report
## https://numpy.org/doc/stable/reference/maskedarray.generic.html#accessing-only-the-valid-entries
## https://www.delftstack.com/howto/numpy/numpy-convert-string-array-to-float-array/
discovery_facility = votable.array['disc_facility'].compressed()
discovery_year = votable.array['disc_year'].compressed()
discovery_year = np.asarray(discovery_year, dtype = float)
distance = votable.array['sy_dist'].compressed()
earth_radius = votable.array['pl_rade'].compressed()
jupiter_radius = votable.array['pl_radj'].compressed()
orbit_period = votable.array['pl_orbper'].compressed()
planet_mass_earth = votable.array['pl_bmasse'].compressed()
planet_orbit_eccentricity = votable.array['pl_orbeccen'].compressed()
planets_in_system = votable.array['sy_pnum'].compressed()
planets_in_system = np.asarray(planets_in_system, dtype = float)
semi_major_axis = votable.array['pl_orbsmax'].compressed()
star_radius = votable.array['st_rad'].compressed()
star_temperature = votable.array['st_teff'].compressed()
stars_in_system = votable.array['sy_snum'].compressed()
stars_in_system = np.asarray(stars_in_system, dtype = float)

# Report Creation
def generate_report(dataset):
    report = report_util.Report("Properties of Exoplanets")

    section = report.add_section("Background")

    paragraph = section.add_paragraph()
    
    paragraph.append(f"This report examines statistical data from the collection of all known exoplanets. ") 
    paragraph.append(f"Starting with charts and moving to text examinations, too. ")
    

    paragraph_2 = section.add_paragraph()
    ##########################################################################
    # The following code demonstrates creating a figure directly with the matplotlib API
    ##########################################################################
    figure_1 = section.add_figure()
    figure_1.caption = "Dataset Histogram"
    ax = figure_1.matplotlib_figure.add_subplot(1,1,1)
    ax.hist(planet_mass_earth, 20000, density = True, facecolor = '#E34234', alpha = 0.75)
    ax.set_xlabel('Multiples of Earth Mass', fontsize = 14).set_color('#393d3f')
    ax.set_ylabel('Probability', fontsize = 14).set_color('#393d3f')
    ax.set_title('Distribution of Planetary Mass', fontsize = 20).set_color('#171819')
    ax.set_xlim(0, 100)
    # Need to find how to customize the chart within this report to my standards.
    figure_1.matplotlib_figure.tight_layout()

    paragraph_2.append_cross_reference(figure_1)
    paragraph_2.append(f" shows the histogram distribution of the numbers in the dataset. ")

    ##########################################################################
    # The following code demonstrates creating another section to the report
    ##########################################################################
    section_2 = report.add_section("More Random Data")
    paragraph_3 = section_2.add_paragraph()

    return report

if __name__ == "__main__":
    np.random.seed(19680801)
    dataset = np.random.randn(50)
    report = generate_report(dataset)

    html_generator = report_util.HTMLReportContext("")
    html_generator.generate(report,"test")
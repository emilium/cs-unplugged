"""Module for the custom Django makeresources command."""

import os
import os.path
from urllib.parse import urlencode
from time import time
from django.core.management.base import BaseCommand
from django.http.request import QueryDict
from resources.models import Resource
from resources.views.views import generate_resource_pdf
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_test_configurations import resource_valid_test_configurations


class Command(BaseCommand):
    """Required command class for the custom Django makestaticresources command."""

    help = "Creates static PDF files of resource combinations."

    def add_arguments(self, parser):
        """Add optional parameter to makeresources command."""
        parser.add_argument(
            "resource_name",
            nargs="?",
            default=None,
            help="The resource name to generate",
        )

    def handle(self, *args, **options):
        """Automatically called when the makeresources command is given."""
        BASE_PATH = "staticfiles/resources/"
        if not os.path.exists(BASE_PATH):
            os.makedirs(BASE_PATH)

        if options["resource_name"]:
            resources = [Resource.objects.get(name=options["resource_name"])]
        else:
            resources = Resource.objects.order_by("name")

        for resource in resources:
            resource_start_time = time()
            print("Creating {}...".format(resource.name))

            # TODO: Import repeated in next for loop, check alternatives
            empty_generator = get_resource_generator(resource.generator_module)
            combinations = resource_valid_test_configurations(
                empty_generator.valid_options,
                header_text=False
            )

            # Create PDF for all possible combinations
            for number, combination in enumerate(combinations):
                start_time = time()
                if resource.copies:
                    combination["copies"] = 30
                requested_options = QueryDict(urlencode(combination, doseq=True))
                generator = get_resource_generator(resource.generator_module, requested_options)
                (pdf_file, filename) = generate_resource_pdf(resource.name, generator)

                filename = "{}.pdf".format(filename)
                pdf_file_output = open(os.path.join(BASE_PATH, filename), "wb")
                pdf_file_output.write(pdf_file)
                pdf_file_output.close()
                print("Created {}".format(filename))
                print("{}{:.1f} secs".format(" " * 4, time() - start_time))
                print("{}{:.0f}% of {} generated".format(
                    " " * 4,
                    (number + 1) / len(combinations) * 100, resource.name
                ))
            print("\n{} took {:.1f} secs to generate all combinations\n".format(
                resource.name,
                time() - resource_start_time
            ))

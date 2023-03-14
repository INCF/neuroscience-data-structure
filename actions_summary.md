# Preface

This file tries to summarise what [the group](https://www.incf.org/sig/incf-working-group-standardized-data.) has been discussing so far.
We hope to facilitate onboarding with this document.

We exists officially since the end of 2020.
We have focused the work on bringing animal data (expecially neuro-, electro-physiology data) into BIDS format.
This is highly related to nwb/nix format and openminds electrophysiology expansion projects.

Julien Colomb initiated this document from reading the [minutes googledoc files](minutes-links.md).
Details about the group members were saved in the [contributors.md](contributors.md) file.

# BIDS consideration

-   BIDS currently does not support linkage between data files obtained at the same time on different subjects. (level 1 is subjects, that would be one unique animal).
-   [BEP for microscopy data](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html) might be interesting to look at (see also [issue](https://github.com/bids-standard/bids-specification/issues/510), [PR](https://github.com/bids-standard/bids-specification/pull/881)). For instance the sample issue [was sorted](https://github.com/bids-standard/bids-specification/pull/816) (together with some of us).

# Set of use cases

### Example

-   Dandi [asset level metadata:](https://api.dandiarchive.org/api/dandisets/000055/versions/draft/assets/ccdc3ae1-e98d-4a17-93d8-5b7386689fe0/)
-   Dandi [example of samples](https://api.dandiarchive.org/api/dandisets/000008/versions/draft/assets/13eb9838-8a09-431e-8724-06a12fabb2d8/):
-   Dandi [example of probes](https://api.dandiarchive.org/api/dandisets/000045/versions/draft/assets/b7855fa3-b6ee-4545-86b4-b4413095876b/):  
-   Dandi [dataset level metadata](https://api.dandiarchive.org/api/dandisets/000008/versions/draft/)
-   openminds [data](https://search.kg.ebrains.eu/instances/33a53fd9-d8ae-4313-9c28-b5921e5a0fee)set
-   [human eeg example](https://www.humanbrainproject.eu/en/follow-hbp/news/localize-mi-an-open-source-dataset-of-simultaneous-intracerebral-stimulation-and-hd-eeg-in-humans/)

\

# BEP032: Electrophy data 

The group has been discussing how to use the power of nwb and nix format, while having a BIDS format.

## Type of data

patch clamp data is included in bep032 (work done during brainhack 2021), `Microelectrode Recordings` ( BEP0206) may be a special case of electrophysiology ?
BEP 026 and 032 to be merge ?

## Files combinations

-   BIDS requires different data files for different modalities (electrophy data, behavior recording, ..., meaning different data collection equipment) , while nwb/nix combine them.
-   Several sessions/run will be included in nix/nwb, BIDS should get session specific files

Proposed restrictions for NWB / NIX files as they would be used in BIDS: - can not contain multiple modalities - can not contain data from multiple (BIDS) sessions - should be accompanied by one sidecar file (which can contain a hierarchical structure)

## Dealing with runs

One session may include different experimental "runs".

# metadata

## Decisions

-   one set of metadata files for each run (redundant but simpler)

## Schemas and ontologies

### age categories

<http://purl.obolibrary.org/obo/UBERON_0000105>

### Spatial position of probes

-    diversity of keys collected to be reduced
-    issues
    -   differentiate between target location vs actual location

    -   consider location corrections or changes to be stored in different runs

    -   allow for uncertainties

    -   maybe consider start coordinate and end coordinate ?

    -   alignment methods are typically post-processes and should maybe be considered as derivatives

### Examples of schemas

Schemas and ontologies for dealing with probes, electrodes, nerve cuffs, etc. and the intersection between location (both semantic and spatial) and data acquisition and actuation/stimulation.

[GitHub dandi-cli issue related to issues with modelling probes](https://github.com/dandi/dandi-cli/issues/642#issuecomment-845623408)

[SPARC recommendations for physiology (work in progress)](https://docs.google.com/document/d/1-mADY7Rnev1jbtNBvlEX5nHNf8FD2YsNCTPGI-8k27w/edit#)

[BEP 32 animal physiology extension](https://docs.google.com/document/d/1oG-C8T-dWPqfVzL2W8HO3elWK8NIh2cOCPssRGv23n0/edit#heading=h.4k1noo90gelw)

<https://pynwb.readthedocs.io/en/stable/pynwb.ecephys.html>

<https://pynwb.readthedocs.io/en/stable/pynwb.icephys.html>

<https://github.com/HumanBrainProject/openMINDS_SANDS>

<https://github.com/HumanBrainProject/openMINDS_ephys> (work in progress)

<https://www.incf.org/sig/incf-working-group-electrophysiology-stimulation-ontology>

<https://www.incf.org/sig/incf-working-group-standardized-data>

# Relation and tools

-   Openminds :links needed here: openminds for electrophysiology expansion.

```{=html}
<!-- -->
```
-   NWB: [best practice](ttps://www.nwb.org/best-practices/) -\> inspector (command line tool to check practices), different from a validation tool. See also [NeuroConv](http://neuroconv.readthedocs.io): library for converting data to NWB
-   Conversion tool : <https://gin.g-node.org/RemiGau/example_ephys_bids_conversion>

```{=html}
<!-- -->
```
-   other tools
    -   BEAVERDAM (build, explore, and visualize experiment databases of metadata; early version, in development), translate BIDS to \"database\"

    -   ALPACA (automated light-weight provenance tracking), provenance + ontology for analysis method

    -   <https://github.com/INCF/artem-is>

    -   [BEADL](https://beadl.org):  design, communicate, and disseminate behavioral task descriptions

        \

## 

## Current main TO DOs

1.  BEP 032 finishing and merge

2.  Keep on having these discussions to identify specific points that need to be harmonized between projects (e.g metadata in dandi and openminds) 

3.  Gathering info about all conversion tools between the different formats into a single place could be a good practical contribution from our group!

4.  Setting milestones on the development of tools to convert data into BIDS

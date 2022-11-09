from enum import Enum


class BirdColumns(Enum):
    GBIFID                              = "gbifID"
    ABSTRACT                            = "abstract"
    ACCESSRIGHTS                        = "accessRights"
    ACCRUALMETHOD                       = "accrualMethod"
    ACCRUALPERIODICITY                  = "accrualPeriodicity"
    ACCRUALPOLICY                       = "accrualPolicy"
    ALTERNATIVE                         = "alternative"
    AUDIENCE                            = "audience"
    AVAILABLE                           = "available"
    BIBLIOGRAPHICCITATION               = "bibliographicCitation"
    CONFORMSTO                          = "conformsTo"
    CONTRIBUTOR                         = "contributor"
    COVERAGE                            = "coverage"
    CREATED                             = "created"
    CREATOR                             = "creator"
    DATE                                = "date"
    DATEACCEPTED                        = "dateAccepted"
    DATECOPYRIGHTED                     = "dateCopyrighted"
    DATESUBMITTED                       = "dateSubmitted"
    DESCRIPTION                         = "description"
    EDUCATIONLEVEL                      = "educationLevel"
    EXTENT                              = "extent"
    FORMAT                              = "format"
    HASFORMAT                           = "hasFormat"
    HASPART                             = "hasPart"
    HASVERSION                          = "hasVersion"
    IDENTIFIER                          = "identifier"
    INSTRUCTIONALMETHOD                 = "instructionalMethod"
    ISFORMATOF                          = "isFormatOf"
    ISPARTOF                            = "isPartOf"
    ISREFERENCEDBY                      = "isReferencedBy"
    ISREPLACEDBY                        = "isReplacedBy"
    ISREQUIREDBY                        = "isRequiredBy"
    ISVERSIONOF                         = "isVersionOf"
    ISSUED                              = "issued"
    LANGUAGE                            = "language"
    LICENSE                             = "license"
    MEDIATOR                            = "mediator"
    MEDIUM                              = "medium"
    MODIFIED                            = "modified"
    PROVENANCE                          = "provenance"
    PUBLISHER                           = "publisher"
    REFERENCES                          = "references"
    RELATION                            = "relation"
    REPLACES                            = "replaces"
    REQUIRES                            = "requires"
    RIGHTS                              = "rights"
    RIGHTSHOLDER                        = "rightsHolder"
    SOURCE                              = "source"
    SPATIAL                             = "spatial"
    SUBJECT                             = "subject"
    TABLEOFCONTENTS                     = "tableOfContents"
    TEMPORAL                            = "temporal"
    TITLE                               = "title"
    TYPE                                = "type"
    VALID                               = "valid"
    INSTITUTIONID                       = "institutionID"
    COLLECTIONID                        = "collectionID"
    DATASETID                           = "datasetID"
    INSTITUTIONCODE                     = "institutionCode"
    COLLECTIONCODE                      = "collectionCode"
    DATASETNAME                         = "datasetName"
    OWNERINSTITUTIONCODE                = "ownerInstitutionCode"
    BASISOFRECORD                       = "basisOfRecord"
    INFORMATIONWITHHELD                 = "informationWithheld"
    DATAGENERALIZATIONS                 = "dataGeneralizations"
    DYNAMICPROPERTIES                   = "dynamicProperties"
    OCCURRENCEID                        = "occurrenceID"
    CATALOGNUMBER                       = "catalogNumber"
    RECORDNUMBER                        = "recordNumber"
    RECORDEDBY                          = "recordedBy"
    RECORDEDBYID                        = "recordedByID"
    INDIVIDUALCOUNT                     = "individualCount"
    ORGANISMQUANTITY                    = "organismQuantity"
    ORGANISMQUANTITYTYPE                = "organismQuantityType"
    SEX                                 = "sex"
    LIFESTAGE                           = "lifeStage"
    REPRODUCTIVECONDITION               = "reproductiveCondition"
    BEHAVIOR                            = "behavior"
    ESTABLISHMENTMEANS                  = "establishmentMeans"
    DEGREEOFESTABLISHMENT               = "degreeOfEstablishment"
    PATHWAY                             = "pathway"
    GEOREFERENCEVERIFICATIONSTATUS      = "georeferenceVerificationStatus"
    OCCURRENCESTATUS                    = "occurrenceStatus"
    PREPARATIONS                        = "preparations"
    DISPOSITION                         = "disposition"
    ASSOCIATEDOCCURRENCES               = "associatedOccurrences"
    ASSOCIATEDREFERENCES                = "associatedReferences"
    ASSOCIATEDSEQUENCES                 = "associatedSequences"
    ASSOCIATEDTAXA                      = "associatedTaxa"
    OTHERCATALOGNUMBERS                 = "otherCatalogNumbers"
    OCCURRENCEREMARKS                   = "occurrenceRemarks"
    ORGANISMID                          = "organismID"
    ORGANISMNAME                        = "organismName"
    ORGANISMSCOPE                       = "organismScope"
    ASSOCIATEDORGANISMS                 = "associatedOrganisms"
    PREVIOUSIDENTIFICATIONS             = "previousIdentifications"
    ORGANISMREMARKS                     = "organismRemarks"
    MATERIALSAMPLEID                    = "materialSampleID"
    EVENTID                             = "eventID"
    PARENTEVENTID                       = "parentEventID"
    FIELDNUMBER                         = "fieldNumber"
    EVENTDATE                           = "eventDate"
    EVENTTIME                           = "eventTime"
    STARTDAYOFYEAR                      = "startDayOfYear"
    ENDDAYOFYEAR                        = "endDayOfYear"
    YEAR                                = "year"
    MONTH                               = "month"
    DAY                                 = "day"
    VERBATIMEVENTDATE                   = "verbatimEventDate"
    HABITAT                             = "habitat"
    SAMPLINGPROTOCOL                    = "samplingProtocol"
    SAMPLESIZEVALUE                     = "sampleSizeValue"
    SAMPLESIZEUNIT                      = "sampleSizeUnit"
    SAMPLINGEFFORT                      = "samplingEffort"
    FIELDNOTES                          = "fieldNotes"
    EVENTREMARKS                        = "eventRemarks"
    LOCATIONID                          = "locationID"
    HIGHERGEOGRAPHYID                   = "higherGeographyID"
    HIGHERGEOGRAPHY                     = "higherGeography"
    CONTINENT                           = "continent"
    WATERBODY                           = "waterBody"
    ISLANDGROUP                         = "islandGroup"
    ISLAND                              = "island"
    COUNTRYCODE                         = "countryCode"
    STATEPROVINCE                       = "stateProvince"
    COUNTY                              = "county"
    MUNICIPALITY                        = "municipality"
    LOCALITY                            = "locality"
    VERBATIMLOCALITY                    = "verbatimLocality"
    VERBATIMELEVATION                   = "verbatimElevation"
    VERTICALDATUM                       = "verticalDatum"
    VERBATIMDEPTH                       = "verbatimDepth"
    MINIMUMDISTANCEABOVESURFACEINMETERS = "minimumDistanceAboveSurfaceInMeters"
    MAXIMUMDISTANCEABOVESURFACEINMETERS = "maximumDistanceAboveSurfaceInMeters"
    LOCATIONACCORDINGTO                 = "locationAccordingTo"
    LOCATIONREMARKS                     = "locationRemarks"
    DECIMALLATITUDE                     = "decimalLatitude"
    DECIMALLONGITUDE                    = "decimalLongitude"
    COORDINATEUNCERTAINTYINMETERS       = "coordinateUncertaintyInMeters"
    COORDINATEPRECISION                 = "coordinatePrecision"
    POINTRADIUSSPATIALFIT               = "pointRadiusSpatialFit"
    VERBATIMCOORDINATESYSTEM            = "verbatimCoordinateSystem"
    VERBATIMSRS                         = "verbatimSRS"
    FOOTPRINTWKT                        = "footprintWKT"
    FOOTPRINTSRS                        = "footprintSRS"
    FOOTPRINTSPATIALFIT                 = "footprintSpatialFit"
    GEOREFERENCEDBY                     = "georeferencedBy"
    GEOREFERENCEDDATE                   = "georeferencedDate"
    GEOREFERENCEPROTOCOL                = "georeferenceProtocol"
    GEOREFERENCESOURCES                 = "georeferenceSources"
    GEOREFERENCEREMARKS                 = "georeferenceRemarks"
    GEOLOGICALCONTEXTID                 = "geologicalContextID"
    EARLIESTEONORLOWESTEONOTHEM         = "earliestEonOrLowestEonothem"
    LATESTEONORHIGHESTEONOTHEM          = "latestEonOrHighestEonothem"
    EARLIESTERAORLOWESTERATHEM          = "earliestEraOrLowestErathem"
    LATESTERAORHIGHESTERATHEM           = "latestEraOrHighestErathem"
    EARLIESTPERIODORLOWESTSYSTEM        = "earliestPeriodOrLowestSystem"
    LATESTPERIODORHIGHESTSYSTEM         = "latestPeriodOrHighestSystem"
    EARLIESTEPOCHORLOWESTSERIES         = "earliestEpochOrLowestSeries"
    LATESTEPOCHORHIGHESTSERIES          = "latestEpochOrHighestSeries"
    EARLIESTAGEORLOWESTSTAGE            = "earliestAgeOrLowestStage"
    LATESTAGEORHIGHESTSTAGE             = "latestAgeOrHighestStage"
    LOWESTBIOSTRATIGRAPHICZONE          = "lowestBiostratigraphicZone"
    HIGHESTBIOSTRATIGRAPHICZONE         = "highestBiostratigraphicZone"
    LITHOSTRATIGRAPHICTERMS             = "lithostratigraphicTerms"
    GROUP                               = "group"
    FORMATION                           = "formation"
    MEMBER                              = "member"
    BED                                 = "bed"
    IDENTIFICATIONID                    = "identificationID"
    VERBATIMIDENTIFICATION              = "verbatimIdentification"
    IDENTIFICATIONQUALIFIER             = "identificationQualifier"
    TYPESTATUS                          = "typeStatus"
    IDENTIFIEDBY                        = "identifiedBy"
    IDENTIFIEDBYID                      = "identifiedByID"
    DATEIDENTIFIED                      = "dateIdentified"
    IDENTIFICATIONREFERENCES            = "identificationReferences"
    IDENTIFICATIONVERIFICATIONSTATUS    = "identificationVerificationStatus"
    IDENTIFICATIONREMARKS               = "identificationRemarks"
    TAXONID                             = "taxonID"
    SCIENTIFICNAMEID                    = "scientificNameID"
    ACCEPTEDNAMEUSAGEID                 = "acceptedNameUsageID"
    PARENTNAMEUSAGEID                   = "parentNameUsageID"
    ORIGINALNAMEUSAGEID                 = "originalNameUsageID"
    NAMEACCORDINGTOID                   = "nameAccordingToID"
    NAMEPUBLISHEDINID                   = "namePublishedInID"
    TAXONCONCEPTID                      = "taxonConceptID"
    SCIENTIFICNAME                      = "scientificName"
    ACCEPTEDNAMEUSAGE                   = "acceptedNameUsage"
    PARENTNAMEUSAGE                     = "parentNameUsage"
    ORIGINALNAMEUSAGE                   = "originalNameUsage"
    NAMEACCORDINGTO                     = "nameAccordingTo"
    NAMEPUBLISHEDIN                     = "namePublishedIn"
    NAMEPUBLISHEDINYEAR                 = "namePublishedInYear"
    HIGHERCLASSIFICATION                = "higherClassification"
    KINGDOM                             = "kingdom"
    PHYLUM                              = "phylum"
    CLASS                               = "class"
    ORDER                               = "order"
    FAMILY                              = "family"
    SUBFAMILY                           = "subfamily"
    GENUS                               = "genus"
    GENERICNAME                         = "genericName"
    SUBGENUS                            = "subgenus"
    INFRAGENERICEPITHET                 = "infragenericEpithet"
    SPECIFICEPITHET                     = "specificEpithet"
    INFRASPECIFICEPITHET                = "infraspecificEpithet"
    CULTIVAREPITHET                     = "cultivarEpithet"
    TAXONRANK                           = "taxonRank"
    VERBATIMTAXONRANK                   = "verbatimTaxonRank"
    VERNACULARNAME                      = "vernacularName"
    NOMENCLATURALCODE                   = "nomenclaturalCode"
    TAXONOMICSTATUS                     = "taxonomicStatus"
    NOMENCLATURALSTATUS                 = "nomenclaturalStatus"
    TAXONREMARKS                        = "taxonRemarks"
    DATASETKEY                          = "datasetKey"
    PUBLISHINGCOUNTRY                   = "publishingCountry"
    LASTINTERPRETED                     = "lastInterpreted"
    ELEVATION                           = "elevation"
    ELEVATIONACCURACY                   = "elevationAccuracy"
    DEPTH                               = "depth"
    DEPTHACCURACY                       = "depthAccuracy"
    DISTANCEABOVESURFACE                = "distanceAboveSurface"
    DISTANCEABOVESURFACEACCURACY        = "distanceAboveSurfaceAccuracy"
    ISSUE                               = "issue"
    MEDIATYPE                           = "mediaType"
    HASCOORDINATE                       = "hasCoordinate"
    HASGEOSPATIALISSUES                 = "hasGeospatialIssues"
    TAXONKEY                            = "taxonKey"
    ACCEPTEDTAXONKEY                    = "acceptedTaxonKey"
    KINGDOMKEY                          = "kingdomKey"
    PHYLUMKEY                           = "phylumKey"
    CLASSKEY                            = "classKey"
    ORDERKEY                            = "orderKey"
    FAMILYKEY                           = "familyKey"
    GENUSKEY                            = "genusKey"
    SUBGENUSKEY                         = "subgenusKey"
    SPECIESKEY                          = "speciesKey"
    SPECIES                             = "species"
    ACCEPTEDSCIENTIFICNAME              = "acceptedScientificName"
    VERBATIMSCIENTIFICNAME              = "verbatimScientificName"
    TYPIFIEDNAME                        = "typifiedName"
    PROTOCOL                            = "protocol"
    LASTPARSED                          = "lastParsed"
    LASTCRAWLED                         = "lastCrawled"
    REPATRIATED                         = "repatriated"
    RELATIVEORGANISMQUANTITY            = "relativeOrganismQuantity"
    LEVEL0GID                           = "level0Gid"
    LEVEL0NAME                          = "level0Name"
    LEVEL1GID                           = "level1Gid"
    LEVEL1NAME                          = "level1Name"
    LEVEL2GID                           = "level2Gid"
    LEVEL2NAME                          = "level2Name"
    LEVEL3GID                           = "level3Gid"
    LEVEL3NAME                          = "level3Name"
    IUCNREDLISTCATEGORY                 = "iucnRedListCategory"

"""
ElewaSTEM Pan-African Data Protection & Jurisdictional Compliance Matrix
Maps African countries to their national Data Protection Authorities (DPAs), Children's Privacy Sections, and AU Malabo Convention guidelines.
"""

from typing import Dict, List, Any

PAN_AFRICAN_DPA_REGISTRY: Dict[str, Dict[str, Any]] = {
    "KE": {
        "country": "Kenya",
        "flag": "🇰🇪",
        "law_name": "Data Protection Act, 2019",
        "regulatory_body": "Office of the Data Protection Commissioner (ODPC)",
        "child_data_section": "Section 29 (Processing of Personal Data Relating to Children)",
        "consent_requirement": "Explicit, verifiable parental/guardian consent required before processing any child telemetric or location data.",
        "edge_processing_mandate": "Designed to support compliance via zero-cloud retention and client-side on-device geolocation mapping.",
        "cross_border_transfer_rules": "Permitted with adequate safeguards (Section 48/49); ElewaSTEM operates local-first."
    },
    "NG": {
        "country": "Nigeria",
        "flag": "🇳🇬",
        "law_name": "Nigeria Data Protection Act, 2023 (NDPA)",
        "regulatory_body": "Nigeria Data Protection Commission (NDPC)",
        "child_data_section": "Section 31 (Processing of Personal Data of a Child)",
        "consent_requirement": "Parental consent required for children under 18; strict duty of care regarding educational tools.",
        "edge_processing_mandate": "Adheres to data minimization principles; no sensitive identifiers stored.",
        "cross_border_transfer_rules": "Strict adequacy criteria under Section 41-43; full on-device execution prevents unauthorized cross-border exposure."
    },
    "ZA": {
        "country": "South Africa",
        "flag": "🇿🇦",
        "law_name": "Protection of Personal Information Act, 2013 (POPIA)",
        "regulatory_body": "Information Regulator (South Africa)",
        "child_data_section": "Section 34 & 35 (Prohibition and Authorization on Processing Personal Information of Children)",
        "consent_requirement": "General prohibition on processing child data unless competent person consents or in the child's educational best interest.",
        "edge_processing_mandate": "Zero profiling of minors; local storage only on device hardware.",
        "cross_border_transfer_rules": "Supports Section 72 alignment; no cloud transmission of student interaction records."
    },
    "GH": {
        "country": "Ghana",
        "flag": "🇬🇭",
        "law_name": "Data Protection Act, 2012 (Act 843)",
        "regulatory_body": "Data Protection Commission (DPC Ghana)",
        "child_data_section": "Section 37 & 38 (Special Personal Data & Children)",
        "consent_requirement": "Parental assent required; educational data must be used strictly for pedagogical purposes.",
        "edge_processing_mandate": "Strict purpose limitation and local data custody.",
        "cross_border_transfer_rules": "Regulated under Section 45."
    },
    "UG": {
        "country": "Uganda",
        "flag": "🇺🇬",
        "law_name": "Data Protection and Privacy Act, 2019",
        "regulatory_body": "Personal Data Protection Office (PDPO Uganda / NITA-U)",
        "child_data_section": "Section 8 (Data on Children)",
        "consent_requirement": "Prohibits processing data of children without prior written/digital consent of a parent or legal guardian.",
        "edge_processing_mandate": "Enforced through zero-knowledge offline client PWA architecture.",
        "cross_border_transfer_rules": "Section 19 requirements met via local execution."
    },
    "TZ": {
        "country": "Tanzania",
        "flag": "🇹🇿",
        "law_name": "Personal Data Protection Act, 2022",
        "regulatory_body": "Personal Data Protection Commission (PDPC Tanzania)",
        "child_data_section": "Section 30 (Special Categories & Protection of Children)",
        "consent_requirement": "Explicit consent for processing minors' data; local storage preference.",
        "edge_processing_mandate": "Designed to support compliance through on-device offline storage.",
        "cross_border_transfer_rules": "Section 31 regulations respected."
    },
    "RW": {
        "country": "Rwanda",
        "flag": "🇷🇼",
        "law_name": "Law No. 058/2021 relating to the Protection of Personal Data and Privacy",
        "regulatory_body": "National Cyber Security Authority (NCSA Rwanda)",
        "child_data_section": "Article 10 (Processing of Personal Data of a Child)",
        "consent_requirement": "Requires consent from parents/legal guardians for persons under 16 years.",
        "edge_processing_mandate": "Complete data minimization and instant revocation.",
        "cross_border_transfer_rules": "Article 48 adequacy conditions fulfilled."
    },
    "AU_CONTINENTAL": {
        "country": "Pan-African Union",
        "flag": "🌍",
        "law_name": "African Union Malabo Convention on Cyber Security and Personal Data Protection (2014)",
        "regulatory_body": "African Union Commission (AUC)",
        "child_data_section": "Article 14 & Article 15 (Principles of Personal Data Processing)",
        "consent_requirement": "Legitimacy, fairness, and fundamental human dignity in all digital education tools across member states.",
        "edge_processing_mandate": "Promotes African digital sovereignty through local on-device AI processing.",
        "cross_border_transfer_rules": "Harmonized cross-border framework for digital single market."
    }
}


def get_privacy_framework(country_code: str = "KE") -> Dict[str, Any]:
    return PAN_AFRICAN_DPA_REGISTRY.get(country_code.upper(), PAN_AFRICAN_DPA_REGISTRY["KE"])


def get_all_jurisdictions() -> List[Dict[str, Any]]:
    return list(PAN_AFRICAN_DPA_REGISTRY.values())

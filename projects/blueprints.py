from __future__ import annotations

import json

try:
    from projects.common import ProductBlueprint
except ModuleNotFoundError:  # Allows `python projects/blueprints.py` from the repository root.
    from common import ProductBlueprint

BLUEPRINTS = [
    ProductBlueprint("Cited Knowledge Assistant", "SME operations teams", "Staff repeatedly search policy documents", "Answer with source IDs in under 15 seconds", "Approve knowledge-base changes", 149, 8, 6, 20),
    ProductBlueprint("Document Intelligence", "Accounting and logistics firms", "Manual re-keying of PDFs creates delay and errors", "Extract validated fields with exception queue", "Review low-confidence fields", 99, 12, 5, 15),
    ProductBlueprint("Voice Receptionist", "Clinics and local services", "Missed calls become missed bookings", "Resolve or route calls with confirmed summary", "Approve sensitive or high-impact actions", 249, 35, 15, 35),
    ProductBlueprint("E-commerce Catalog Engine", "Retailers and exporters", "SKU content is slow and inconsistent", "Publish approved multilingual product packs", "Approve factual claims and images", 129, 10, 5, 20),
    ProductBlueprint("Localization Studio", "Educators and media teams", "Localization requires many manual handoffs", "Deliver timed transcript, translation and voice plan", "Consent and final language review", 199, 30, 8, 30),
    ProductBlueprint("Property Media Studio", "Real estate and tourism teams", "Listings lack consistent media and copy", "Create factual listing package from approved assets", "Approve representations and disclosures", 79, 14, 4, 12),
    ProductBlueprint("Support Triage", "Customer support teams", "Queues mix routine and urgent requests", "Classify, retrieve, draft and escalate", "Agent approves external replies", 179, 18, 8, 28),
    ProductBlueprint("Proposal Copilot", "Agencies and B2B vendors", "RFP requirements are missed", "Build traceable requirement matrix and draft", "Owner approves every commitment", 119, 10, 4, 22),
    ProductBlueprint("Niche Tutor", "Training providers", "Learners need adaptive practice", "Grounded lessons, quizzes and feedback", "Instructor approves source set", 19, 2, 1, 3),
    ProductBlueprint("Market Intelligence Brief", "Small strategy teams", "Signals are fragmented across sources", "Deliver cited weekly brief with changes", "Analyst approves conclusions", 99, 14, 5, 18),
]

if __name__ == "__main__":
    print(json.dumps([item.report() for item in BLUEPRINTS], indent=2))

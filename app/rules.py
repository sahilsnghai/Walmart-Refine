import re

from app.logger import logger
BANNED_WORDS = ["cosplay", "weapon", "knife", "UV", "premium", "perfect"]

def check_violations(data):

    logger.info("checking for violationss. ")
    violations = []

    text = " ".join(str(v) for v in data.values()).lower()

    for word in BANNED_WORDS:
        if word.lower() in text:
            violations.append(f"banned_word:{word}")

    if len(data.get("meta_title", "")) > 70:
        violations.append("meta_title > 70chars")

    if len(data.get("meta_description", "")) > 160:
        violations.append("meta_description > 160chars")

    if "key_features_html" in data:
        bullets = re.findall(r"<li>(.*?)</li>", data["key_features_html"])
        if len(bullets) > 8:
            violations.append("too_many_bullets")
        if any(len(b) > 85 for b in bullets):
            violations.append("bullet_too_long")

    if violations:
        logger.exception(f"Violations found {violations} ")

    return ", ".join(violations) if violations else ""

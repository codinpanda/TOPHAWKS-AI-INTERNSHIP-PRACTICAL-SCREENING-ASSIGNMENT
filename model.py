def calculate_lead_score(pricing_page_time, demo_requested, visits, email_clicks):
    """
    Calculates a lead score based on a simple rule-based system.
    """
    score = 30  # Base score
    
    # Pricing page time > 5 → +25
    if pricing_page_time > 5:
        score += 25
        
    # Demo requested → +30
    if demo_requested == "Yes" or demo_requested is True:
        score += 30
        
    # Visits > 10 → +15
    if visits > 10:
        score += 15
        
    # Email clicks > 3 → +10
    if email_clicks > 3:
        score += 10
        
    # Cap score at 100
    return min(score, 100)

def get_priority(score):
    """
    Returns priority based on the score.
    """
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"

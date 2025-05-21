def apply_tags(order):
    if order.test_type in ["CBC", "PCR", "T4"]:
        order.tags.append("high_priority")
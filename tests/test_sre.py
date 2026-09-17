import unittest
from app.burn import Window,response
from app.deploy import assess
class SRE(unittest.TestCase):
 def test_sustained_burn_pages(self): self.assertEqual(response(Window(15,100,5),Window(7,100,60),.99),"page_and_pause_risky_rollouts")
 def test_healthy_is_within_policy(self): self.assertEqual(response(Window(0,100,5),Window(0,100,60),.99),"within_policy")
 def test_deployment_rejects_latest_and_missing_probe(self):
  self.assertEqual(assess({"spec":{"containers":[{"image":"api:latest"}]}}),"reject_mutable_image")
  self.assertEqual(assess({"spec":{"containers":[{"image":"api:1"}]}}),"reject_missing_readiness_probe")

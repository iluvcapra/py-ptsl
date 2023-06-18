# from typing import Optional
from unittest import TestCase
from unittest.mock import Mock, patch

# import grpc


from ptsl.PTSL_pb2 import GetPTSLVersionResponseBody
from ptsl.engine import open_engine
import ptsl.ops as ops


class TestEngine(TestCase):

    def test_get_version(self):
        def ret_version(op: ops.Operation):
            op.response = GetPTSLVersionResponseBody(version=1)
            return
        
        with patch('ptsl.Client'):
            with open_engine(company_name="none", application_name="none") as engine:
                with patch.object(engine.client, 'run', new=Mock(side_effect=ret_version)):
                    self.assertIsNotNone(engine)
                    self.assertEqual(engine.ptsl_version(),1)
                    engine.client.run.assert_called()

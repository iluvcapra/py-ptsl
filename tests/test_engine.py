from typing import Optional, Any
from unittest import TestCase
from unittest.mock import Mock, patch
from contextlib import contextmanager

from ptsl.PTSL_pb2 import GetPTSLVersionResponseBody
from ptsl.engine import open_engine
import ptsl.ops as ops

@contextmanager 
def open_engine_with_mock_client(run_response=Optional[Any]):
    with patch('ptsl.Client'):
        with open_engine(company_name="none", application_name="none") as engine:
            if run_response is None:
                yield engine
            else:
                def give_response(op: ops.Operation):
                    op.response = run_response
                
                with patch.object(engine.client, 'run', new=Mock(side_effect=give_response)):
                    yield engine

class TestEngine(TestCase):

    def test_ptsl_version(self):
        with open_engine_with_mock_client(run_response=GetPTSLVersionResponseBody(version=1)) as engine:
            self.assertIsNotNone(engine)
            self.assertEqual(engine.ptsl_version(),1)
            engine.client.run.assert_called()

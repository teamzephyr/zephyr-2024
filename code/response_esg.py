from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class MetaData:
    question: str = ""
    esgType: str = ""
    esgIndicators: str = ""
    primaryDetails: str = ""
    secondaryDetails: str = ""
    citationDetails: str = ""
    pageNumber: int = 0

@dataclass
class Metrics:
    timeTaken: int = 0
    leveragedModel: str = ""

@dataclass
class ResponseInternalDetails:
    entityName: str = ""
    benchmarkDetails: List[MetaData] = field(default_factory=list)
    metrics: Metrics = Metrics()

@dataclass
class ResponseInternalDetailsScalar:
    entityName: str = ""
    benchmarkDetails: MetaData = MetaData()
    metrics: Metrics = Metrics()
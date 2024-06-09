from enum import Enum, IntEnum
from pydantic import BaseModel, conint, PlainSerializer
from typing import Optional
from typing_extensions import Annotated


class TitleEnum(str, Enum):
    ai_automation = 'ai_automation'
    backend = 'backend'
    crm = 'crm'
    data_analytics = 'data_analytics'
    data_engineer = 'data_engineer'
    data_scientist = 'data_scientist'
    devops_sre_platform = 'devops_sre_platform'
    embedded = 'embedded'
    engineering_manager = 'engineering_manager'
    executive = 'executive'
    frontend = 'frontend'
    fullstack = 'fullstack'
    hardware = 'hardware'
    mobile = 'mobile'
    product_manager = 'product_manager'
    product_owner = 'product_owner'
    research = 'research'
    scrum = 'scrum'
    security = 'security'
    system_arch = 'system_arch'
    technical_support = 'technical_support'
    testing = 'testing'
    ui_ux = 'ui_ux'


class LevelEnum(str, Enum):
    c_level = 'c_level'
    director = 'director'
    group_product_manager = 'group_product_manager'
    intern_level = 'intern'
    junior = 'junior'
    manager = 'manager'
    mid_level = 'mid_level'
    principal = 'principal'
    senior = 'senior'
    senior_manager = 'senior_manager'
    senior_principal = 'senior_principal'
    senior_staff = 'senior_staff'
    staff = 'staff'
    team_lead = 'team_lead'
    vp = 'vp'


class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class DegreeEnum(str, Enum):
    cs = "yes"
    non_cs = "no"


class BusinessMarketEnum(str, Enum):
    global_market = "global"
    regional_market = "regional"
    local_market = "local"


class BusinessSizeEnum(str, Enum):
    large = "large"
    medium = "medium"
    small = "small"


class BusinessFocusEnum(str, Enum):
    product = "product"
    software = "software_house"


class BusinessLineEnum(str, Enum):
    b2b = "b2b"
    b2c = "b2c"
    both = "both"


class ProgrammingLanguageEnum(str, Enum):
    javascript = "java_script"
    typescript = "type_script"
    python = "python"
    c_sharp = "c_sharp"
    java = "java"
    php = "php"
    c_plus_plus = "c_cplusplus"
    kotlin = "kotlin"
    swift = "swift"
    dart = "dart"
    go = "go"
    r = "r"
    scala = "scala"
    rust = "rust"


DegreeType = Annotated[bool, PlainSerializer(lambda x: "yes" if x else "no")]
IncludeType = Annotated[bool, PlainSerializer(lambda x: "true" if x else "false")]


class ParticipantsQueryParams(BaseModel):
    title: Optional[TitleEnum] = None
    level: Optional[LevelEnum] = None
    min_yoe: Optional[conint(strict=True, ge=0, le=20)] = None
    max_yoe: Optional[conint(strict=True, ge=1, le=26)] = None
    gender: Optional[GenderEnum] = None
    cs_degree: Optional[DegreeType] = None
    business_market: Optional[BusinessMarketEnum] = None
    business_size: Optional[BusinessSizeEnum] = None
    business_focus: Optional[BusinessFocusEnum] = None
    business_line: Optional[BusinessLineEnum] = None
    include_relocated: Optional[IncludeType] = None
    include_remote_abroad: Optional[IncludeType] = None


class StatsQueryParams(ParticipantsQueryParams):
    programming_language: Optional[ProgrammingLanguageEnum] = None

from enum import Enum, IntEnum
from pydantic import BaseModel, conint, PlainSerializer, ConfigDict
from typing import Optional
from typing_extensions import Annotated


class TitleEnum(str, Enum):
    """Enum for the job title of participants retrieved from the API."""
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
    """Enum for the job level of participants retrieved from the API."""
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
    """Enum for the gender of participants retrieved from the API."""
    male = "male"
    female = "female"


class BusinessMarketEnum(str, Enum):
    """Enum for the market scope of the business of participants retrieved from the API."""
    global_market = "global"
    regional_market = "regional"
    local_market = "local"


class BusinessSizeEnum(str, Enum):
    """Enum for the size of the business of participants retrieved from the API."""
    large = "large"
    medium = "medium"
    small = "small"


class BusinessFocusEnum(str, Enum):
    """Enum for the focus of the business of participants retrieved from the API."""
    product = "product"
    software = "software_house"


class BusinessLineEnum(str, Enum):
    """Enum for the line of business of participants retrieved from the API."""
    b2b = "b2b"
    b2c = "b2c"
    both = "both"


class ProgrammingLanguageEnum(str, Enum):
    """Enum for the programming language of participants retrieved from the API."""
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
    """Model for the query parameters of the participants endpoint of the API.

    Attributes
    ----------
    title : TitleEnum
        The job title of the participants.
    level : LevelEnum
        The job level of the participants.
    min_yoe : int
        The minimum years of experience of the participants.
    max_yoe : int
        The maximum years of experience of the participants.
    gender : GenderEnum
        The gender of the participants.
    cs_degree : DegreeType
        Whether the participants have a computer science degree.
    business_market : BusinessMarketEnum
        The market scope of the business of the participants.
    business_size : BusinessSizeEnum
        The size of the business of the participants.
    business_focus : BusinessFocusEnum
        The focus of the business of the participants.
    business_line : BusinessLineEnum
        The line of business of the participants.
    include_relocated : IncludeType
        Whether to include participants who have relocated.
    include_remote_abroad : IncludeType
        Whether to include participants who are remote abroad.

    """
    model_config = ConfigDict(extra='forbid')
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
    """Model for the query parameters of the stats endpoint of the API.

    Attributes
    ----------
    title : TitleEnum
        The job title of the participants.
    level : LevelEnum
        The job level of the participants.
    min_yoe : int
        The minimum years of experience of the participants.
    max_yoe : int
        The maximum years of experience of the participants.
    gender : GenderEnum
        The gender of the participants.
    cs_degree : DegreeType
        Whether the participants have a computer science degree.
    business_market : BusinessMarketEnum
        The market scope of the business of the participants.
    business_size : BusinessSizeEnum
        The size of the business of the participants.
    business_focus : BusinessFocusEnum
        The focus of the business of the participants.
    business_line : BusinessLineEnum
        The line of business of the participants.
    include_relocated : IncludeType
        Whether to include participants who have relocated.
    include_remote_abroad : IncludeType
        Whether to include participants who are remote abroad.

    programming_language : ProgrammingLanguageEnum
        The programming language of the participants.

        """
    model_config = ConfigDict(extra='forbid')

    programming_language: Optional[ProgrammingLanguageEnum] = None

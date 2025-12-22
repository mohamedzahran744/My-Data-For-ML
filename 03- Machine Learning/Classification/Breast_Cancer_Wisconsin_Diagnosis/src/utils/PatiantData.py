from pydantic import BaseModel


class PatiantData(BaseModel):
    """
    Pydantic model for validating patient input data.
    
    Contains the top 10 features most correlated with breast cancer diagnosis.
    These features are extracted from digitized images of breast mass fine needle aspirate (FNA).
    
    All measurements are numerical values representing characteristics of cell nuclei.
    """
    
    # Worst (largest) values of concave points - mean of the three largest values
    # Concave points measure the number of concave portions of the cell nucleus contour
    concave_points_worst: float
    
    # Worst (largest) perimeter measurement of the cell nucleus
    perimeter_worst: float
    
    # Mean value of concave points across all cell nuclei in the sample
    concave_points_mean: float 
    
    # Worst (largest) radius measurement - distance from center to perimeter
    radius_worst: float
    
    # Mean perimeter measurement of cell nuclei
    perimeter_mean: float
    
    # Worst (largest) area measurement of the cell nucleus
    area_worst: float
    
    # Mean radius measurement across all cell nuclei
    radius_mean: float
    
    # Mean area measurement of cell nuclei
    area_mean: float
    
    # Mean severity of concave portions of the cell nucleus contour
    concavity_mean: float
    
    # Worst (largest) concavity measurement
    concavity_worst: float
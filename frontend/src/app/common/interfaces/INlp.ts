export interface INlp {
    id: number,
    tag: string,
    description: string,
    patterns: Pattern[],
    responses: Response[]
}
  
export interface Pattern {
    id: number,
    pattern_text: string,
    intent_id: number
}
  
export interface Response {
    id: number,
    response_text: string,
    intent_id: number
}